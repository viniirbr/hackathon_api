import { Injectable } from '@nestjs/common';
import { PrismaService } from 'prisma/prisma.service';
import arsenal from '../../../data/ManCity_Arsenal_events.json';
import astonvilla from '../../../data/ManCity_AstonVilla_events.json';
import brighton from '../../../data/ManCity_Brighton_events.json';
import leicester from '../../../data/ManCity_LeicesterCity_events.json';
import liverpool from '../../../data/ManCity_Liverpool_events.json';
import tottenham from '../../../data/ManCity_Tottenham_events.json';

const events = [
  ...arsenal,
  ...astonvilla,
  ...brighton,
  ...leicester,
  ...liverpool,
  ...tottenham,
];

@Injectable()
export class EventTypeSeeder {
  constructor(private readonly prismaService: PrismaService) {}
  async seed() {
    events.forEach(async (event) => {
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
