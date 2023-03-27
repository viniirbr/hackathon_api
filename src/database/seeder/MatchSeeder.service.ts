import { Injectable } from '@nestjs/common';
import { Prisma } from '@prisma/client';
import { PrismaService } from 'prisma/prisma.service';
import arsenal from '../../../data/ManCity_Arsenal_lineups.json';
import astonVilla from '../../../data/ManCity_AstonVilla_lineups.json';
import brighton from '../../../data/ManCity_Brighton_lineups.json';
import leicester from '../../../data/ManCity_LeicesterCity_lineups.json';
import liverpool from '../../../data/ManCity_Liverpool_lineups.json';
import tottenham from '../../../data/ManCity_Tottenham_lineups.json';

const matches = [
  arsenal,
  astonVilla,
  brighton,
  leicester,
  liverpool,
  tottenham,
];

@Injectable()
export class MatchSeeder {
  constructor(private readonly prismaService: PrismaService) {}
  async seed() {
    matches.forEach(async (match) => {
      const result = await this.prismaService.match.findFirst({
        where: {
          opponentId:
            match[0].team_id === 746 ? match[1].team_id : match[0].team_id,
        },
      });

      if (result === null) {
        await this.prismaService.match.create({
          data: {
            date: new Date('2023-01-01'),
            opponent: {
              connect: { id: match[1].team_id },
            },
          },
          include: {
            opponent: true,
          },
        });
      }
    });
  }
}
