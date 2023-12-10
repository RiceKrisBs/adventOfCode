# frozen_string_literal: true

require_relative 'base'
require 'set'

class Day < Base
  def part_1
    connections, current_pos, raw_map = parse_input
    path_length = 0
    visited = Set.new
    loop do
      break if connections[current_pos].nil?
      path_length += 1
      visited << current_pos
      current_pos = connections[current_pos].find { |point| !visited.include?(point) }
    end
    path_length / 2
  end

  def part_2
    connections, current_pos, raw_map = parse_input
    path_length = 0
    visited = Set.new
    loop do
      break if connections[current_pos].nil?
      path_length += 1
      visited << current_pos
      current_pos = connections[current_pos].find { |point| !visited.include?(point) }
    end
    new_map = map_of_visited_points(raw_map, visited)

    p new_map.map(&:join)
    # Now you have a pretty picture in your terminal...
    # Go manually count them like I did ¯\_(ツ)_/¯ 
  end

  private

  TESTING = false
  DAY = '10'
  
  def input
    TESTING ? File.join('inputs', "input#{DAY}-test.txt") : File.join('inputs', "input#{DAY}.txt")
  end

  def parse_input
    data = File.read(input).split("\n")
    raw_map = data.map { |line| line.split('') }
    connections = {}
    starting_point = nil
    data.each_with_index do |line, row|
      line.each_char.with_index do |char, col|
        next if char == '.'
        connections[[row, col]] = [[row-1,col],[row+1,col]] if char == '|'
        connections[[row, col]] = [[row,col-1],[row,col+1]] if char == '-'
        connections[[row, col]] = [[row-1,col],[row,col+1]] if char == 'L'
        connections[[row, col]] = [[row,col-1],[row-1,col]] if char == 'J'
        connections[[row, col]] = [[row,col-1],[row+1,col]] if char == '7'
        connections[[row, col]] = [[row,col+1],[row+1,col]] if char == 'F'
        if char == 'S'
          starting_point = [row,col]
          s_points = []
          if data[row-1][col] == '|' || data[row-1][col] == '7' || data[row-1][col] == 'F'
            s_points << [row-1,col]
          end
          if data[row+1][col] == '|' || data[row+1][col] == 'L' || data[row+1][col] == 'J'
            s_points << [row+1,col]
          end
          if data[row][col-1] == '-' || data[row][col-1] == 'L' || data[row][col-1] == 'F'
            s_points << [row,col-1]
          end
          if data[row][col+1] == '-' || data[row][col+1] == 'J' || data[row][col+1] == '7'
            s_points << [row,col+1]
          end
          connections[[row,col]] = s_points
        end

      end
    end
    return connections, starting_point, raw_map
  end

  def map_of_visited_points(raw_map, visited_points)
    bad_to_good = {'|'=>'│', '-'=>'─', 'L'=>'└', 'J'=>'┘', '7'=>'┐', 'F'=>'┌', 'S'=>'S'}
    readable_map = raw_map.map.with_index do |row, r|
      row.map.with_index do |char, c|
        if visited_points.include?([r,c])
          bad_to_good[char]
        else
          '.'
        end
      end
    end
  end
end

# Day.new.run
puts "Part 1: #{Day.new.part_1}"
puts Day.new.part_2
# Day.new.benchmark
