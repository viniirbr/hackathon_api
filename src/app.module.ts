import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { SeederModule } from './database/seeder/seeder.module';
import { PlayerModule } from './player/player.module';

@Module({
  imports: [SeederModule, PlayerModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
