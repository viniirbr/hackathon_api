-- RedefineTables
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_Player" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "createdAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" DATETIME NOT NULL,
    "weigth" REAL NOT NULL,
    "height" REAL NOT NULL,
    "observations" TEXT NOT NULL,
    "available" BOOLEAN NOT NULL DEFAULT true
);
INSERT INTO "new_Player" ("createdAt", "height", "id", "name", "observations", "updatedAt", "weigth") SELECT "createdAt", "height", "id", "name", "observations", "updatedAt", "weigth" FROM "Player";
DROP TABLE "Player";
ALTER TABLE "new_Player" RENAME TO "Player";
CREATE TABLE "new_Team" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "abrv" TEXT NOT NULL DEFAULT ''
);
INSERT INTO "new_Team" ("id", "name") SELECT "id", "name" FROM "Team";
DROP TABLE "Team";
ALTER TABLE "new_Team" RENAME TO "Team";
PRAGMA foreign_key_check;
PRAGMA foreign_keys=ON;
