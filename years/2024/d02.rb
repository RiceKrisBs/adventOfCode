# frozen_string_literal: true

require_relative 'base'

class Day < Base
  def part_1
    data = File.read(input).split("\n")
    data.map do |line|
      levels = line.split.map(&:to_i)
      report_safe?(levels) ? 1 : 0
    end.sum
  end

  def part_2
    data = File.read(input).split("\n")
    data.map do |line|
      levels = line.split.map(&:to_i)
      report_safe?(levels) || report_safe_with_dampner?(levels) ? 1 : 0
    end.sum
  end

  private

  def report_safe?(report)
    diffs = report[...-1].zip(report[1...]).map { |a, b| b - a }
    return false unless diffs.all?(&:positive?) || diffs.all?(&:negative?)
    return false unless diffs.map(&:abs).all? { |diff| 1 <= diff && diff <= 3 }

    true
  end

  def report_safe_with_dampner?(report)
    possible_reports = report.combination(report.size - 1)
    possible_reports.any? { |report| report_safe?(report) }
  end

  TESTING = false
  DAY = '02'

  def input
    TESTING ? File.join('inputs', "input#{DAY}-test.txt") : File.join('inputs', "input#{DAY}.txt")
  end
end

Day.new.run_part_1
Day.new.run_part_2
# Day.new.benchmark
