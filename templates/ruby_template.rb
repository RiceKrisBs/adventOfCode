# frozen_string_literal: true

require_relative 'base'

class Day < Base
  def part_1
    data = File.read(input).split("\n")
    data.map do |line|
      # implementation goes here
    end
    nil
  end

  def part_2
    data = File.read(input).split("\n")
    data.map do |line|
      # implementation goes here
    end
    nil
  end

  private

  TESTING = true
  DAY = ''
  
  def input
    TESTING ? File.join('inputs', "input#{DAY}-test.txt") : File.join('inputs', "input#{DAY}.txt")
  end
end

Day.new.run_part_1
Day.new.run_part_2
# Day.new.benchmark
