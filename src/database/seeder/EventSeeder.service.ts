import { Injectable } from '@nestjs/common';
import { PrismaService } from 'prisma/prisma.service';

// import arsenal from '../../../data/ManCity_Arsenal_events.json';
// import astonvilla from '../../../data/ManCity_AstonVilla_events.json';
// import brighton from '../../../data/ManCity_Brighton_events.json';
// import leicester from '../../../data/ManCity_LeicesterCity_events.json';
// import liverpool from '../../../data/ManCity_Liverpool_events.json';
import tottenham from '../../../data/ManCity_Tottenham_events.json';

const matches = [
  // {
  //   matchId: 6,
  //   events: arsenal.filter(
  //     (event) => event.team.id === 746 && event.type.id === 40,
  //   ),
  // },
  // {
  //   matchId: 7,
  //   events: astonvilla.filter(
  //     (event) => event.team.id === 746 && event.type.id === 40,
  //   ),
  // },
  // {
  //   matchId: 8,
  //   events: brighton.filter(
  //     (event) => event.team.id === 746 && event.type.id === 40,
  //   ),
  // },
  // {
  //   matchId: 9,
  //   events: liverpool.filter(
  //     (event) => event.team.id === 746 && event.type.id === 40,
  //   ),
  // },
  // {
  //   matchId: 10,
  //   events: leicester.filter(
  //     (event) => event.team.id === 746 && event.type.id === 40,
  //   ),
  // },
  {
    matchId: 11,
    events: tottenham.filter(
      (event) => event.team.id === 746 && event.type.id === 40,
    ),
  },
];

@Injectable()
export class EventSeeder {
  constructor(private readonly prismaService: PrismaService) {}
  async seed() {
    matches.forEach((match) => {
      (match.events as any).forEach(async (event) => {
        const result = await this.prismaService.event.findFirst({
          where: {
            id: event.id,
          },
        });
        if (result === null) {
          if (event.player) {
            await this.prismaService.event.create({
              data: {
                id: event.id,
                minutes: event.minute,
                type: {
                  connect: { id: event.type.id },
                },
                player: {
                  connect: { id: event.player.id },
                },
                team: {
                  connect: { id: event?.team.id },
                },
                match: {
                  connect: { id: match.matchId },
                },
              },
            });
          } else {
            await this.prismaService.event.create({
              data: {
                id: event.id,
                minutes: event.minute,
                type: {
                  connect: { id: event.type.id },
                },
                team: {
                  connect: { id: event?.team.id },
                },
                match: {
                  connect: { id: match.matchId },
                },
              },
            });
          }
        }
      });
    });
  }
}
