import { Logger, Module } from '@nestjs/common';
import { PrismaService } from 'prisma/prisma.service';
import { PlayerSeeder } from './PlayersSeeder.service';
import { EventTypeSeeder } from './EventTypeSeeder.service';
import { TeamSeeder } from './TeamSeeder.service';
import { MatchSeeder } from './MatchSeeder.service';

@Module({
  providers: [
    PlayerSeeder,
    PrismaService,
    Logger,
    EventTypeSeeder,
    TeamSeeder,
    MatchSeeder,
  ],
})
export class SeederModule {}
