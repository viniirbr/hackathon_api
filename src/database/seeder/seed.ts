import { Logger } from '@nestjs/common';
import { NestFactory } from '@nestjs/core';
import { PlayerSeeder } from './PlayersSeeder.service';
import { EventTypeSeeder } from './EventTypeSeeder.service';
import { SeederModule } from './seeder.module';
import { TeamSeeder } from './TeamSeeder.service';
import { MatchSeeder } from './MatchSeeder.service';
import { EventSeeder } from './EventSeeder.service';
import { PlayersStatsSeeder } from './PlayersStatsSeeder.service';
import { FormationMatchSeeder } from './FormationMatchSeeder.service';

async function bootstrap() {
  const appContext = await NestFactory.createApplicationContext(SeederModule);
  const logger = appContext.get(Logger);
  const playerSeeder = appContext.get(PlayerSeeder);
  const eventTypeSeeder = appContext.get(EventTypeSeeder);
  const teamSeeder = appContext.get(TeamSeeder);
  const matchSeeder = appContext.get(MatchSeeder);
  const eventSeeder = appContext.get(EventSeeder);
  const playerStatsSeeder = appContext.get(PlayersStatsSeeder);
  const formationMatchSeeder = appContext.get(FormationMatchSeeder);
  // try {
  //   await playerSeeder.seed();
  //   logger.debug('Seeding complete!');
  // } catch (error) {
  //   logger.error('Seeding failed!');
  //   throw error;
  // } finally {
  //   appContext.close();
  // }

  // try {
  //   await eventTypeSeeder.seed();
  //   logger.debug('Seeding complete!');
  // } catch (error) {
  //   logger.error('Seeding failed!');
  //   throw error;
  // } finally {
  //   appContext.close();
  // }

  // try {
  //   await teamSeeder.seed();
  //   logger.debug('Seeding complete!');
  // } catch (error) {
  //   logger.error('Seeding failed!');
  //   throw error;
  // } finally {
  //   appContext.close();
  // }

  // try {
  //   await matchSeeder.seed();
  //   logger.debug('Seeding complete!');
  // } catch (error) {
  //   logger.error('Seeding failed!');
  //   throw error;
  // } finally {
  //   appContext.close();
  // }

  // try {
  //   await eventSeeder.seed();
  //   logger.debug('Seeding complete!');
  // } catch (error) {
  //   logger.error('Seeding failed!');
  //   throw error;
  // } finally {
  //   appContext.close();

  // try {
  //   await playerStatsSeeder.seed();
  //   logger.debug('Seeding complete!');
  // } catch (error) {
  //   logger.error('Seeding failed!');
  //   throw error;
  // } finally {
  //   appContext.close();
  // }

  try {
    await formationMatchSeeder.seed();
    logger.debug('Seeding complete!');
  } catch (error) {
    logger.error('Seeding failed!');
    throw error;
  } finally {
    appContext.close();
  }
}
bootstrap();
