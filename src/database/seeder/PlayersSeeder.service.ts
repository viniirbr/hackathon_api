import { Injectable } from '@nestjs/common';
import { PrismaService } from 'prisma/prisma.service';
import data from '../../../data/ManCity_Arsenal_lineups.json';

@Injectable()
export class PlayerSeeder {
  constructor(private readonly prismaService: PrismaService) {}
  async seed() {
    const team = data.find((item) => item.team_id === 746);
    team.lineup.forEach(async (player) => {
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
