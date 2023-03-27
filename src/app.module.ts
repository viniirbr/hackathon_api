import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { SeederModule } from './database/seeder/seeder.module';
import { EventSeedService } from './database/seeder/EventSeeder.service';
import { MatchSeederService } from './database/seeder/MatchSeeder.service';

@Module({
  imports: [SeederModule],
  controllers: [AppController],
  providers: [AppService, EventSeedService, MatchSeederService],
})
export class AppModule {}
