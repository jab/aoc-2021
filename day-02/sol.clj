#!/usr/bin/env bb

(ns day2
  (:require [clojure.string :as str]))


(defn parse-input [input]
  (->> input
       str/split-lines
       (map #(str/split % #"\s"))
       (map (fn [[cmd n]] [cmd (Integer/parseInt n)]))))


(def example-input (parse-input "forward 5
down 5
forward 8
up 3
down 8
forward 2
"))

(def my-input (parse-input (slurp "input.txt")))

(defn part1 [input]
  (->> input
       (reduce
         (fn [[hpos depth] [cmd n]]
           (case cmd
             "up" [hpos (- depth n)]
             "down" [hpos (+ depth n)]
             "forward" [(+ hpos n) depth]))
        [0 0])
       (apply *)))

(defn part2 [input]
  (->> input
       (reduce
         (fn [[hpos depth aim] [cmd n]]
           (case cmd
             "up" [hpos depth (- aim n)]
             "down" [hpos depth (+ aim n)]
             "forward" [(+ hpos n) (+ depth (* aim n)) aim]))
        [0 0 0])
       butlast
       (apply *)))


(prn (part1 example-input) 150)
(prn (part2 example-input) 900)
(prn (part1 my-input) 1561344)
(prn (part2 my-input) 1848454425)
