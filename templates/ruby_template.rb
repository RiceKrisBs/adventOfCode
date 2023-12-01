# frozen_string_literal: true

class Day
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

  TESTING = false
  DAY = ''
  
  def input
    TESTING ? File.join('inputs', "input#{DAY}-test.txt") : File.join('inputs', "input#{DAY}.txt")
  end
end

puts("Part 1: #{Day.new.part_1}")
puts("Part 2: #{Day.new.part_2}")
