import { Injectable } from '@nestjs/common';
import { PrismaService } from 'prisma/prisma.service';

const teams = [
  {
    id: 968,
    name: 'Arsenal WFC',
  },
  {
    id: 2647,
    name: 'Aston Villa',
  },
  {
    id: 965,
    name: 'Brighton & Hove Albion WFC',
  },
  {
    id: 2652,
    name: 'Leicester City WFC',
  },
  {
    id: 966,
    name: 'Liverpool WFC',
  },
  {
    id: 749,
    name: 'Tottenham Hotspur Women',
  },
];

@Injectable()
export class TeamSeeder {
  constructor(private readonly prismaService: PrismaService) {}
  async seed() {
    teams.forEach(async (team) => {
      const result = await this.prismaService.team.findUnique({
        where: {
          id: team.id,
        },
      });
      if (result === null) {
        await this.prismaService.team.create({
          data: {
            id: team.id,
            name: team.name,
          },
        });
      }
    });
  }
}
