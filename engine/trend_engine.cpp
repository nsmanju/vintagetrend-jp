#include <sqlite3.h>
#include <iostream>
#include <fstream>
#include <string>

int main() {
    sqlite3* db;
    if(sqlite3_open("data/vintage.db", &db)) {
        std::cerr << "Can't open DB\n";
        return 1;
    }

    const char* sql = R"(
        SELECT title, source, AVG(price) as avg_price, COUNT(*) as cnt
        FROM listings
        WHERE scraped_at > datetime('now','-1 day') AND currency='JPY'
        GROUP BY title, source
        ORDER BY cnt DESC LIMIT 20;
    )";

    sqlite3_stmt* stmt;
    sqlite3_prepare_v2(db, sql, -1, &stmt, nullptr);

    std::ofstream out("dashboard/trends.json");
    out << "[\n";
    bool first=true;
    while(sqlite3_step(stmt)==SQLITE_ROW){
        if(!first) out << ",\n"; 
        first=false;
        std::string title = (char*)sqlite3_column_text(stmt,0);
        std::string source = (char*)sqlite3_column_text(stmt,1);
        double avg = sqlite3_column_double(stmt,2);
        int cnt = sqlite3_column_int(stmt,3);
        for(auto &c: title) if(c=='"') c='\'';
        out << "  {\"title\":\"" << title << "\", \"source\":\"" << source << "\", \"avg_price\":" << avg << ", \"count\":" << cnt << ", \"currency\":\"JPY\"}";
    }
    out << "\n]\n";
    sqlite3_finalize(stmt);
    sqlite3_close(db);
    std::cout << "Japan trends written to dashboard/trends.json\n";
    return 0;
}
