import { Injectable } from '@nestjs/common';
import { PrismaService } from 'prisma/prisma.service';

@Injectable()
export class FormationService {
  constructor(private readonly prismaService: PrismaService) {}

  listAll() {
    return this.prismaService.formation.findMany({});
  }
}
