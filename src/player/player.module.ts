import { Module } from '@nestjs/common';
import { PlayerService } from './player.service';
import { PrismaService } from 'prisma/prisma.service';
import { PlayerController } from './player.controller';

@Module({
  providers: [PlayerService, PrismaService],
  controllers: [PlayerController],
})
export class PlayerModule {}
