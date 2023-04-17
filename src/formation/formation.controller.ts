import { Controller, Get } from '@nestjs/common';
import { FormationService } from './formation.service';

@Controller('formation')
export class FormationController {
  constructor(private readonly formationService: FormationService) {}

  @Get()
  listAll() {
    return this.formationService.listAll();
  }
}
