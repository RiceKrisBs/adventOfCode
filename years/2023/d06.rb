# frozen_string_literal: true

require_relative 'base'

class Day < Base
  def part_1
    data = File.read(input).split("\n")
    data.map! do |line|
      line.split[1..].map(&:to_i)
    end
    races = data.first.length
    ways_to_win = []
    races.times do |i|
      time = data[0][i]
      dist = data[1][i]
      w = 0
      (0..time).each do |time_held|
        remaining_time = time - time_held
        distance_travelled = time_held * remaining_time
        w += 1 if distance_travelled > dist
      end
      ways_to_win << w
    end
    ways_to_win.inject(:*)
  end

  def part_2
    data = File.read(input).split("\n")
    data.map! do |line|
      [line.split[1..].inject(:+).to_i]
    end
    races = data.first.length
    ways_to_win = []
    races.times do |i|
      time = data[0][i]
      dist = data[1][i]
      w = 0
      (0..time).each do |time_held|
        remaining_time = time - time_held
        distance_travelled = time_held * remaining_time
        w += 1 if distance_travelled > dist
      end
      ways_to_win << w
    end
    ways_to_win.inject(:*)
  end

  private

  TESTING = false
  DAY = '06'
  
  def input
    TESTING ? File.join('inputs', "input#{DAY}-test.txt") : File.join('inputs', "input#{DAY}.txt")
  end
end

Day.new.run
# Day.new.benchmark
