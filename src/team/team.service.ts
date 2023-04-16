import { Injectable } from '@nestjs/common';
import { PrismaService } from 'prisma/prisma.service';

@Injectable()
export class TeamService {
  constructor(private readonly prismaService: PrismaService) {}

  listAll() {
    return this.prismaService.team.findMany({});
  }

  deleteAll() {
    return this.prismaService.team.deleteMany({});
  }

  setAbrv(teamId: number, abrv: string) {
    console.log(abrv);
    return this.prismaService.team.update({
      where: {
        id: teamId,
      },
      data: {
        abrv: abrv,
      },
    });
  }
}
