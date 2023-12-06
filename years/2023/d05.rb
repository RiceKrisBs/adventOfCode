# frozen_string_literal: true

require_relative 'base'

class Day < Base
  def part_1
    seeds, conversions = parse_input
    seeds.map do |seed|
      i = seed
      conversions.each do |name, mappings|
        i = source_to_destination(input: i, mappings: mappings)
      end
      i
    end.min
  end

  def part_2
    return nil
    seed_parts, conversions = parse_input
    seed_ranges = [] # [[79,93],[55,68]]
    seed_parts.each_slice(2) { |a, b| seed_ranges << [a, a + b] }

    conversions.each do |name, mappings| # iterate over each conversion
      new_seed_ranges = [] # accumulate the seed ranges for the next conversion
      while seed_ranges.length > 0 do # iterate over the seed ranges for the current conversion
        range_start, range_end = seed_ranges.pop # get the bounds of the current seed range
        mappings.each do |mapping| # iterate over each mapping to see if it intersects with the current seed range
          # if we have an upper half mapping, put the upper half into new_seed_ranges and put the lower half into seed_ranges
          # if we have a lower half mapping, put the lower half into new_seed_ranges and put the upper half into seed_ranges
          # if we have a middle mapping, put the middle into new_seed_ranges and put both the upper and lower halves into seed_ranges
          # if there is no overlap, put into seed_ranges
        end
        # if there is anything left in seed_ranges, put them into new_seed_ranges
      end
      seed_ranges = new_seed_ranges
    end
    # find the smallest lower bound in seed_ranges
  end

  private

  TESTING = false
  DAY = '05'

  def input
    TESTING ? File.join('inputs', "input#{DAY}-test.txt") : File.join('inputs', "input#{DAY}.txt")
  end

  def parse_input
    data = File.read(input).split("\n\n")
    seeds = data.shift.split[1..].map(&:to_i)

    conversions = data.each_with_object({}) do |conversion, hash|
      l = conversion.split(/(?:\smap:)?\n/)
      name = l.shift
      mappings = l.map do |mapping|
        mapping.split.map(&:to_i)
      end
      hash[name] = mappings
    end
    return seeds, conversions
  end

  def source_to_destination(input:, mappings:)
    mappings.each do |mapping|
      r = mapping[1]...(mapping[1] + mapping[2])
      if r.include?(input)
        return input - mapping[1] + mapping[0]
      end
    end
  input
  end

end

Day.new.run
# Day.new.benchmark
