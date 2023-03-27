import { Injectable } from '@nestjs/common';
import { PrismaService } from 'prisma/prisma.service';
import data from '../../../data/ManCity_Arsenal_events.json';

@Injectable()
export class EventSeeder {
  constructor(private readonly prismaService: PrismaService) {}
  async seed() {
    data.forEach(async (event) => {
      const result = await this.prismaService.event.findFirst({
        where: {
          id: event.id,
        },
      });
      if (result === null) {
        await this.prismaService.event.create({
          data: {
            id: event.id,
            minutes: event.
          },
        });
      }
    });
  }
}