import { Injectable } from '@nestjs/common';
import { PrismaService } from 'prisma/prisma.service';

@Injectable()
export class PlayersStatsSeeder {
  constructor(private readonly prismaService: PrismaService) {}
  async seed() {
    const players = await this.prismaService.player.findMany();
    players.forEach(async (player) => {
      const walking = 1392.99;
      const jogging = 2086.79;
      const running = 1270.57;
      const high_speed_running = 289.22;
      const sprinting = 148.57;
      const total =
        walking + jogging + running + high_speed_running + sprinting;
      walking + jogging + running + high_speed_running + sprinting;
      await this.prismaService.playerStats.create({
        data: {
          playerId: player.id,
          matchId: 11,
          minute_from: 0,
          minute_to: 90,
          walking,
          jogging,
          running,
          high_speed_running,
          sprinting,
          distance: Number(total.toFixed(2)),
          max_speed: 28.78,
          average_speed: 6.48,
        },
      });
    });
  }
}
