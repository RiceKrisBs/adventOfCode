# frozen_string_literal: true

require_relative 'base'

class Day < Base
  def part_1
    data = format_input
    part_numbers = []
    data.each_with_index do |row, line_idx|
      current_number = ''
      columns = []
      row.each_with_index do |c, column_idx|
        if digit?(c) # build our number
          current_number += c
          columns << column_idx
        else # number is built - time to look around for symbols
          next if current_number == '' # but only look around if we started building a number e.g. skip if '..'

          surrounding_symbols = []
          surrounding_symbols.push(*data[line_idx-1][(columns.first-1)..(columns.last+1)]) # above
          surrounding_symbols.push(*data[line_idx+1][(columns.first-1)..(columns.last+1)]) # below
          surrounding_symbols.push(data[line_idx][columns.first-1]) # left
          surrounding_symbols.push(data[line_idx][columns.last+1]) # right

          part_numbers << current_number.to_i if surrounding_symbols.any? { |s| symbol?(s) }

          # clean up before next set of numbers
          current_number = ''
          columns = []
          surrounding_symbols = []
        end
      end
    end
    part_numbers.sum
  end

  def part_2
    data = format_input
    gears = {}
    data.each_with_index do |row, line_idx|
      current_number = ''
      columns = []
      row.each_with_index do |c, column_idx|
        if digit?(c) # build our number
          current_number += c
          columns << column_idx
        else # number is built - time to look around for gears
          next if current_number == '' # but only look around if we started building a number e.g. skip if '..'

          surrounding_symbols = []
          surrounding_symbols.push(*data[line_idx-1][(columns.first-1)..(columns.last+1)]) # above
          surrounding_symbols.push(*data[line_idx+1][(columns.first-1)..(columns.last+1)]) # below
          surrounding_symbols.push(data[line_idx][columns.first-1]) # left
          surrounding_symbols.push(data[line_idx][columns.last+1]) # right

          if surrounding_symbols.any? {|s| gear?(s)}
            # check for gears, and add the number to any of the gears' values
            if gear?(data[line_idx][columns.first-1]) # left
              gear_coordinate = [line_idx, columns.first-1]
              gears[gear_coordinate] = [] unless gears.key?(gear_coordinate)
              gears[gear_coordinate] << current_number.to_i
            end
            if gear?(data[line_idx][columns.last+1]) # right
              gear_coordinate = [line_idx, columns.last+1]
              gears[gear_coordinate] = [] unless gears.key?(gear_coordinate)
              gears[gear_coordinate] << current_number.to_i
            end
            # check above and below
            (columns.first-1..columns.last+1).each do |column_number|
              if gear?(data[line_idx-1][column_number]) # above
                gear_coordinate = [line_idx-1, column_number]
                gears[gear_coordinate] = [] unless gears.key?(gear_coordinate)
                gears[gear_coordinate] << current_number.to_i
              end
              if gear?(data[line_idx+1][column_number]) # below
                gear_coordinate = [line_idx+1, column_number]
                gears[gear_coordinate] = [] unless gears.key?(gear_coordinate)
                gears[gear_coordinate] << current_number.to_i
              end
            end
          end

          # reset our local trackers
          current_number = ''
          columns = []
          surrounding_symbols = []
        end
      end
    end

    gears.values.filter { |v| v.length == 2 }.reduce(0) { |sum, values| sum + values.first * values.last }
  end

  private

  TESTING = false
  DAY = '03'

  def input
    TESTING ? File.join('inputs', "input#{DAY}-test.txt") : File.join('inputs', "input#{DAY}.txt")
  end

  def format_input
    # create a padding around the provided schematic so that we don't
    # have to worry about checking an index that doesn't exist when looking
    # at the characters around a number trying to find a symbol
    lines = []
    File.foreach(input) do |line|
      line = ".#{line.chomp}."
      lines << line.split('')
    end
    line_length = lines.first.length
    padding_line = Array.new(line_length) { |_| '.' }
    lines << padding_line
    lines.unshift(padding_line)
  end

  def symbol?(c)
    %w[* = - % & @ $ / + #].include?(c)
  end

  def gear?(c)
    c == '*'
  end

  def digit?(c)
    /\d/.match?(c)
  end
end

Day.new.run
# Day.new.benchmark
