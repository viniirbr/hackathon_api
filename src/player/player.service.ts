import { Injectable } from '@nestjs/common';
import { PrismaService } from 'prisma/prisma.service';

@Injectable()
export class PlayerService {
  constructor(private readonly prismaService: PrismaService) {}

  async listAllPlayers() {
    return await this.prismaService.player.findMany();
  }

  async findPlayerById(id: number) {
    return await this.prismaService.player.findUnique({
      where: { id },
      select: {
        playerStats: {
          select: {
            walking: true,
            jogging: true,
            running: true,
            high_speed_running: true,
            sprinting: true,
            match: {
              select: {
                opponent: true,
                date: true,
              },
            },
          },
        },
      },
    });
  }
}
