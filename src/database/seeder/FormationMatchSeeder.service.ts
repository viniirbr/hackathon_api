import { Injectable } from '@nestjs/common';
import { PrismaService } from 'prisma/prisma.service';
import arsenal from '../../../data/ManCity_Arsenal_lineups.json';
import astonvilla from '../../../data/ManCity_AstonVilla_lineups.json';
import brighton from '../../../data/ManCity_Brighton_lineups.json';
import leicester from '../../../data/ManCity_LeicesterCity_lineups.json';
import liverpool from '../../../data/ManCity_Liverpool_lineups.json';
import tottenham from '../../../data/ManCity_Tottenham_lineups.json';

const lineups = [
  ...arsenal,
  ...astonvilla,
  ...brighton,
  ...leicester,
  ...liverpool,
  ...tottenham,
];

@Injectable()
export class FormationMatchSeeder {
  constructor(private readonly prismaService: PrismaService) {}
  async seed() {
    lineups.forEach(async (lineup, index) => {
      if (lineup.team_id === 746) {
        const matchFound = await this.prismaService.match.findMany({
          where: {
            opponentId: lineups[index + 1].team_id,
          },
        });
        lineup.formations.forEach(async (formation) => {
          const formationFound = await this.prismaService.formation.findMany({
            where: {
              name: formation.formation.toString().split('').join('-'),
            },
          });
          if (matchFound && formationFound) {
            await this.prismaService.formationMatch.create({
              data: {
                formationId: formationFound[0].id,
                period: formation.period,
                matchId: matchFound[0].id,
              },
            });
          }
        });
      }
    });
  }
}
