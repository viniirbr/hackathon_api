import { Controller, Get, Param } from '@nestjs/common';
import { PlayerService } from './player.service';

@Controller('player')
export class PlayerController {
  constructor(private readonly playerService: PlayerService) {}

  @Get()
  listAll() {
    return this.playerService.listAllPlayers();
  }

  @Get(':id')
  findOne(@Param() params) {
    const { id } = params;
    return this.playerService.findPlayerById(Number(id));
  }
}
