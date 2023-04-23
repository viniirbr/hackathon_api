import { Controller, Get, Param, Patch, Body } from '@nestjs/common';
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

  @Patch(':id')
  submitObservation(
    @Param() { id }: { id: string },
    @Body() { observations, available, position }: { observations: string, available: boolean, position: string },
  ) {
    return this.playerService.submitObservations(Number(id), observations, available, position);
  }
}
