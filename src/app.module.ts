import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { SeederModule } from './database/seeder/seeder.module';
import { PlayerModule } from './player/player.module';
import { TeamModule } from './team/team.module';
import { FormationModule } from './formation/formation.module';

@Module({
  imports: [SeederModule, PlayerModule, TeamModule, FormationModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
