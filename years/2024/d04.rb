# frozen_string_literal: true

require_relative 'base'

class Day < Base
  def part_1
    data = File.read(input).split("\n")
    data = pad_input(data)
    total = 0
    data.each_with_index do |row, row_idx|
      row.each_char.each_with_index do |char, col_idx|
        next unless char == 'X'

        # left to right
        total += 1 if row[col_idx + 1] == 'M' && row[col_idx + 2] == 'A' && row[col_idx + 3] == 'S'

        # right to left
        total += 1 if row[col_idx - 1] == 'M' && row[col_idx - 2] == 'A' && row[col_idx - 3] == 'S'

        # top to bottom
        total += 1 if data[row_idx + 1][col_idx] == 'M' && data[row_idx + 2][col_idx] == 'A' && data[row_idx + 3][col_idx] == 'S'

        # bottom to top
        total += 1 if data[row_idx - 1][col_idx] == 'M' && data[row_idx - 2][col_idx] == 'A' && data[row_idx - 3][col_idx] == 'S'

        # top left to bottom right
        total += 1 if data[row_idx + 1][col_idx + 1] == 'M' && data[row_idx + 2][col_idx + 2] == 'A' && data[row_idx + 3][col_idx + 3] == 'S'

        # bottom left to top right
        total += 1 if data[row_idx - 1][col_idx + 1] == 'M' && data[row_idx - 2][col_idx + 2] == 'A' && data[row_idx - 3][col_idx + 3] == 'S'

        # top right to bottom left
        total += 1 if data[row_idx + 1][col_idx - 1] == 'M' && data[row_idx + 2][col_idx - 2] == 'A' && data[row_idx + 3][col_idx - 3] == 'S'

        # bottom right to top left
        total += 1 if data[row_idx - 1][col_idx - 1] == 'M' && data[row_idx - 2][col_idx - 2] == 'A' && data[row_idx - 3][col_idx - 3] == 'S'
      end
    end
    total
  end

  def part_2
    data = File.read(input).split("\n")
    data = pad_input(data)
    total = 0
    data.each_with_index do |row, row_idx|
      row.each_char.each_with_index do |char, col_idx|
        next unless char == 'A'

        # top left to bottom right / top right to bottom left
        # MAS and MAS
        total += 1 if data[row_idx - 1][col_idx - 1] == 'M' && data[row_idx + 1][col_idx + 1] == 'S' && data[row_idx - 1][col_idx + 1] == 'M' && data[row_idx + 1][col_idx - 1] == 'S'
        # MAS and SAM
        total += 1 if data[row_idx - 1][col_idx - 1] == 'M' && data[row_idx + 1][col_idx + 1] == 'S' && data[row_idx - 1][col_idx + 1] == 'S' && data[row_idx + 1][col_idx - 1] == 'M'
        # SAM and MAS
        total += 1 if data[row_idx - 1][col_idx - 1] == 'S' && data[row_idx + 1][col_idx + 1] == 'M' && data[row_idx - 1][col_idx + 1] == 'M' && data[row_idx + 1][col_idx - 1] == 'S'
        # SAM and SAM
        total += 1 if data[row_idx - 1][col_idx - 1] == 'S' && data[row_idx + 1][col_idx + 1] == 'M' && data[row_idx - 1][col_idx + 1] == 'S' && data[row_idx + 1][col_idx - 1] == 'M'
      end
    end
    total
  end

  private

  TESTING = false
  DAY = '04'

  def pad_input(data)
    new_data = []
    new_data << '.' * (data[0].length + 6)
    new_data << '.' * (data[0].length + 6)
    data.each do |line|
      new_data << "...#{line}..."
    end
    new_data << '.' * (data[0].length + 6)
    new_data << '.' * (data[0].length + 6)
    new_data
  end
  
  def input
    TESTING ? File.join('inputs', "input#{DAY}-test.txt") : File.join('inputs', "input#{DAY}.txt")
  end
end

Day.new.run_part_1
Day.new.run_part_2
# Day.new.benchmark
