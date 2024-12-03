# frozen_string_literal: true

require_relative 'base'

class Day < Base
  def part_1
    data = File.read(input).split("\n")
    data.map do |line|
      line.scan(/mul\(\d{1,3},\d{1,3}\)/).sum { |val| mul(val) }
    end.sum
  end

  def part_2
    data = File.read(input).split("\n")
    total = 0
    toggle = true
    data.map do |line|
      line.scan(/do(?:n't)?\(\)|mul\(\d{1,3},\d{1,3}\)/).each do |value|
        if value == "do()"
          toggle = true
        elsif value == "don't()"
          toggle = false
        elsif toggle
          total += mul(value)
        end
      end
    end
    total
  end

  private

  def mul(pattern)
    pattern.scan(/\d{1,3}/).map(&:to_i).reduce(:*)
  end

  TESTING = false
  DAY = '03'

  def input
    TESTING ? File.join('inputs', "input#{DAY}-test.txt") : File.join('inputs', "input#{DAY}.txt")
  end
end

raise unless Day.new.part_1 == 182780583
raise unless Day.new.part_2 == 90772405

Day.new.run_part_1
Day.new.run_part_2
# Day.new.benchmark
