/*
  Warnings:

  - You are about to drop the `Lineup` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the column `lineupId` on the `PlayerStats` table. All the data in the column will be lost.

*/
-- DropTable
PRAGMA foreign_keys=off;
DROP TABLE "Lineup";
PRAGMA foreign_keys=on;

-- RedefineTables
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_PlayerStats" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "matchId" INTEGER NOT NULL DEFAULT 0,
    "playerId" INTEGER NOT NULL,
    "minute_from" INTEGER NOT NULL,
    "minute_to" INTEGER,
    "distance" REAL NOT NULL DEFAULT 0,
    "walking" REAL NOT NULL DEFAULT 0,
    "jogging" REAL NOT NULL DEFAULT 0,
    "running" REAL NOT NULL DEFAULT 0,
    "high_speed_running" REAL NOT NULL DEFAULT 0,
    "sprinting" REAL NOT NULL DEFAULT 0,
    "average_speed" REAL NOT NULL DEFAULT 0,
    "max_speed" REAL NOT NULL DEFAULT 0,
    CONSTRAINT "PlayerStats_playerId_fkey" FOREIGN KEY ("playerId") REFERENCES "Player" ("id") ON DELETE RESTRICT ON UPDATE CASCADE,
    CONSTRAINT "PlayerStats_matchId_fkey" FOREIGN KEY ("matchId") REFERENCES "Match" ("id") ON DELETE RESTRICT ON UPDATE CASCADE
);
INSERT INTO "new_PlayerStats" ("id", "minute_from", "minute_to", "playerId") SELECT "id", "minute_from", "minute_to", "playerId" FROM "PlayerStats";
DROP TABLE "PlayerStats";
ALTER TABLE "new_PlayerStats" RENAME TO "PlayerStats";
PRAGMA foreign_key_check;
PRAGMA foreign_keys=ON;
