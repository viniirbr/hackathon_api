-- RedefineTables
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_PlayerStats" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "lineupId" INTEGER NOT NULL,
    "playerId" INTEGER NOT NULL,
    "minute_from" INTEGER NOT NULL,
    "minute_to" INTEGER,
    CONSTRAINT "PlayerStats_playerId_fkey" FOREIGN KEY ("playerId") REFERENCES "Player" ("id") ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT "PlayerStats_lineupId_fkey" FOREIGN KEY ("lineupId") REFERENCES "Lineup" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);
INSERT INTO "new_PlayerStats" ("id", "lineupId", "minute_from", "minute_to", "playerId") SELECT "id", "lineupId", "minute_from", "minute_to", "playerId" FROM "PlayerStats";
DROP TABLE "PlayerStats";
ALTER TABLE "new_PlayerStats" RENAME TO "PlayerStats";
PRAGMA foreign_key_check;
PRAGMA foreign_keys=ON;
