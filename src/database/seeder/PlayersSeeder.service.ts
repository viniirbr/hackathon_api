import { Injectable } from '@nestjs/common';
import { PrismaService } from 'prisma/prisma.service';
import arsenal from '../../../data/ManCity_Arsenal_lineups.json';
import astonVilla from '../../../data/ManCity_AstonVilla_lineups.json';
import brighton from '../../../data/ManCity_Brighton_lineups.json';
import leicester from '../../../data/ManCity_LeicesterCity_lineups.json';
import liverpool from '../../../data/ManCity_Liverpool_lineups.json';
import tottenham from '../../../data/ManCity_Tottenham_lineups.json';

const matches = [
  ...arsenal,
  ...astonVilla,
  ...brighton,
  ...leicester,
  ...liverpool,
  ...tottenham,
];

@Injectable()
export class PlayerSeeder {
  constructor(private readonly prismaService: PrismaService) {}
  async seed() {
    const cityPlayers = matches
      .filter((match) => match.team_id === 746)
      .map((team) => team.lineup);
    console.log('players', cityPlayers);
    const playersWithoutDuplicates = cityPlayers.filter((element, index) => {
      return cityPlayers.indexOf(element) === index;
    })[0];
    playersWithoutDuplicates.forEach(async (player) => {
      const result = await this.prismaService.player.findFirst({
        where: {
          id: player.player_id,
        },
      });

      if (result === null) {
        await this.prismaService.player.create({
          data: {
            id: player.player_id,
            name: player.player_name,
            height: player.player_height || 0,
            weigth: player.player_weight || 0,
            observations: '',
          },
        });
      }
    });
  }
}
