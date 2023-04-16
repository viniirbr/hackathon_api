import { Controller, Delete, Put, Param, Body, Get } from '@nestjs/common';
import { TeamService } from './team.service';

@Controller('team')
export class TeamController {
  constructor(private readonly teamService: TeamService) {}

  @Get()
  listAll() {
    return this.teamService.listAll();
  }

  @Delete()
  deleteAll() {
    return this.teamService.deleteAll();
  }

  @Put(':id')
  setAbrv(@Param() params: { id: number }, @Body() body: { abrv: string }) {
    return this.teamService.setAbrv(Number(params.id), body.abrv);
  }
}
