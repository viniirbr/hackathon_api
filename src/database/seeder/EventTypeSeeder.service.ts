import { Injectable } from '@nestjs/common';
import { PrismaService } from 'prisma/prisma.service';
import data from '../../../data/ManCity_Arsenal_events.json';

@Injectable()
export class EventTypeSeeder {
  constructor(private readonly prismaService: PrismaService) {}
  async seed() {
    data.forEach(async (event) => {
      const result = await this.prismaService.eventType.findFirst({
        where: {
          id: event.type.id,
          name: event.type.name,
        },
      });
      if (result === null) {
        await this.prismaService.eventType.create({
          data: {
            id: event.type.id,
            name: event.type.name,
          },
        });
      }
    });
  }
}
