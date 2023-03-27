import { Injectable } from '@nestjs/common';
import data from '../data/ManCity_Arsenal_events.json';

@Injectable()
export class AppService {
  getHello() {
    const eventTypes = data
      .map((event) => event.type)
      .filter(
        (value, index, self) =>
          index === self.findIndex((t) => t.name === value.name),
      );
    return data[0];
  }
}
