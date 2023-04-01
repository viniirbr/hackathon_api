import { Logger, Module } from '@nestjs/common';
import { PrismaService } from 'prisma/prisma.service';
import { PlayerSeeder } from './PlayersSeeder.service';
import { EventTypeSeeder } from './EventTypeSeeder.service';
import { TeamSeeder } from './TeamSeeder.service';
import { MatchSeeder } from './MatchSeeder.service';
import { EventSeeder } from './EventSeeder.service';
import { PlayersStatsSeeder } from './PlayersStatsSeeder.service';

@Module({
  providers: [
    PlayerSeeder,
    PrismaService,
    Logger,
    EventTypeSeeder,
    TeamSeeder,
    MatchSeeder,
    EventSeeder,
    PlayersStatsSeeder,
  ],
})
export class SeederModule {}
