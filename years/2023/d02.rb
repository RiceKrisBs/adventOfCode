# frozen_string_literal: true

require_relative 'base'

class Day < Base
  def part_1
    data = File.read(input).split("\n")
    possible_games = []
    rc, gc, bc = 12, 13, 14
    data.map do |line|
      game_part, results_part = line.split(':')
      game_number = game_part.split.last.to_i
      draws = results_part.split(';')
      is_possible = true
      draws.each do |draw|
        colors = draw.split(',').map(&:split)
        colors.each do |count, color|
          case color
          when 'red'
            is_possible = false if count.to_i > rc
          when 'green'
            is_possible = false if count.to_i > gc
          when 'blue'
            is_possible = false if count.to_i > bc
          end
        end
      end
      possible_games << game_number.to_i if is_possible
    end
    possible_games.sum
  end

  def part_2
    data = File.read(input).split("\n")
    powers = []
    data.map do |line|
      results_part = line.split(':').last
      draws = results_part.split(';')
      rc, gc, bc = [], [], []
      draws.each do |draw|
        colors = draw.split(',').map(&:split)
        colors.each do |count, color|
          case color
          when 'red'
            rc << count.to_i
          when 'green'
            gc << count.to_i
          when 'blue'
            bc << count.to_i
          end
        end
      end
      r, g, b = rc.max, gc.max, bc.max
      powers << r * g * b
    end
    powers.sum
  end

  private

  TESTING = false
  DAY = '02'
  
  def input
    TESTING ? File.join('inputs', "input#{DAY}-test.txt") : File.join('inputs', "input#{DAY}.txt")
  end
end

Day.new.run
# Day.new.benchmark
