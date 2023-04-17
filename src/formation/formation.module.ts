import { Module } from '@nestjs/common';
import { FormationService } from './formation.service';
import { FormationController } from './formation.controller';
import { PrismaService } from 'prisma/prisma.service';

@Module({
  controllers: [FormationController],
  providers: [FormationService, PrismaService],
})
export class FormationModule {}
