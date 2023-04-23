-- RedefineTables
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_Player" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "createdAt" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" DATETIME NOT NULL,
    "weigth" REAL NOT NULL,
    "height" REAL NOT NULL,
    "position" TEXT NOT NULL DEFAULT '',
    "observations" TEXT NOT NULL,
    "available" BOOLEAN NOT NULL DEFAULT true
);
INSERT INTO "new_Player" ("available", "createdAt", "height", "id", "name", "observations", "updatedAt", "weigth") SELECT "available", "createdAt", "height", "id", "name", "observations", "updatedAt", "weigth" FROM "Player";
DROP TABLE "Player";
ALTER TABLE "new_Player" RENAME TO "Player";
PRAGMA foreign_key_check;
PRAGMA foreign_keys=ON;
