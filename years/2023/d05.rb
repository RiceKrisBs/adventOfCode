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
    seed_parts, conversions = parse_input
    seed_ranges = []
    seed_parts.each_slice(2) { |a, b| seed_ranges << [a, a + b - 1] }
    new_seed_ranges = nil
    conversions.each do |name, mappings| # iterate over each conversion
      new_seed_ranges = [] # accumulate the seed ranges for the next conversion
      while seed_ranges.length > 0 do # iterate over the seed ranges for the current conversion
        seed_range_start, seed_range_end = seed_ranges.pop # get the inclusive bounds of the current seed range
        mapping_found = false
        mappings.each do |mapping| # iterate over each mapping to see if it intersects with the current seed range
          source_start, source_end = mapping[1], mapping[1] + mapping[2] - 1 # get the inclusive bounds of the current mapping
          mapping_offset = mapping[1] - mapping[0]
          # if we have a completely surrounding mapping, put the whole thing into new_seed_ranges
          if source_start <= seed_range_start && source_end >= seed_range_end
            new_seed_ranges << [seed_range_start - mapping_offset, seed_range_end - mapping_offset]
            mapping_found = true
            break
          end
          # if we have an upper half mapping, put the upper half into new_seed_ranges and put the lower half into seed_ranges
          if source_start <= seed_range_end && source_end >= seed_range_end
            new_seed_ranges << [source_start - mapping_offset, seed_range_end - mapping_offset]
            seed_ranges << [seed_range_start, source_start - 1]
            mapping_found = true
            break
          end
          # if we have a lower half mapping, put the lower half into new_seed_ranges and put the upper half into seed_ranges
          if source_start <= seed_range_start && source_end >= seed_range_start
            new_seed_ranges << [seed_range_start - mapping_offset, source_end - mapping_offset]
            seed_ranges << [source_end + 1, seed_range_end]
            mapping_found = true
            break
          end
          # if we have a middle mapping, put the middle into new_seed_ranges and put both the upper and lower halves into seed_ranges
          if source_start >= seed_range_start && source_end <= seed_range_end
            new_seed_ranges << [source_start - mapping_offset, source_end - mapping_offset]
            seed_ranges << [seed_range_start, source_start - 1]
            seed_ranges << [source_end + 1, seed_range_end]
            mapping_found = true
            break
          end
        end
        # put the range into new_seed_ranges if no mapping was found
        new_seed_ranges.push([seed_range_start, seed_range_end]) unless mapping_found
      end
      seed_ranges = new_seed_ranges
    end
    seed_ranges.map(&:first).min
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
