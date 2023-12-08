# frozen_string_literal: true

require_relative 'base'

class Day < Base
  def part_1
    instructions, paths = parse_input
    steps = 0
    l = instructions.length
    current_location = "AAA"

    loop do
      break if current_location == "ZZZ"
      steps += 1
      idx = (steps - 1) % l
      turn = instructions[idx]
      current_location = paths[current_location][turn]
    end

    steps
  end

  def part_2
    instructions, paths = parse_input
    l = instructions.length
    locations = paths.keys.select { |k| k.end_with?("A") }

    locations.map do |location|
      steps = 0
      current_location = location
      loop do
        break if current_location.end_with?("Z")
        steps += 1
        idx = (steps - 1) % l
        turn = instructions[idx]
        current_location = paths[current_location][turn]
      end
      steps
    end.reduce(&:lcm)
  end

  private

  TESTING = false
  DAY = '08'
  
  def input
    TESTING ? File.join('inputs', "input#{DAY}-test.txt") : File.join('inputs', "input#{DAY}.txt")
  end

  def parse_input
    instructions, connections = File.read(input).split("\n\n")

    paths = connections.split("\n").each_with_object({}) do |line, hash|
      data = line.match(/(?<start>\w{3}).+(?<left>\w{3}).+(?<right>\w{3})/)
      hash[data[:start]] = { "L" => data[:left], "R" => data[:right] }
    end

    return instructions, paths
  end
end

Day.new.run
# Day.new.benchmark
