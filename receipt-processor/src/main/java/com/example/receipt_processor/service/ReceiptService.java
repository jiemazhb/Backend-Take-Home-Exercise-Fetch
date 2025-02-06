package com.example.receipt_processor.service;


import com.example.receipt_processor.model.Item;
import com.example.receipt_processor.model.ReceiptRequest;
import org.springframework.stereotype.Service;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

@Service
public class ReceiptService {
    private final Map<String, Integer> myDatabase = new ConcurrentHashMap<>();

    public String processReceipt(ReceiptRequest receipt) {

            String id = UUID.randomUUID().toString();
            int points = calculation(receipt);
            myDatabase.put(id, points);
            return id;

    }

    public Optional<Integer> getPoints(String id) {

        return Optional.ofNullable(myDatabase.get(id));
    }

    private int calculation(ReceiptRequest receipt) {
        int points = 0;

        // One point for every alphanumeric character in the retailer name.
        int count = 0;
        for (char c : receipt.getRetailer().toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                count++;
            }
        }
        points += count;

        //50 points if the total is a round dollar amount with no cents.
        double total = Double.parseDouble(receipt.getTotal());
        if (total % 1 == 0) {
            points += 50;
        }
        // 25 points if the total is a multiple of 0.25.
        if (total % 0.25 == 0) {
            points += 25;
        }
        // 5 points for every two items on the receipt.
        points += (receipt.getItems().size() / 2) * 5;

        // If the trimmed length of the item description is a multiple of 3,
        // multiply the price by 0.2 and round up to the nearest integer.
        // The result is the number of points earned.
        for (Item item : receipt.getItems()) {
            String productDes = item.getShortDescription().trim();
            if (productDes.length() % 3 == 0) {
                points += Math.ceil(Double.parseDouble(item.getPrice()) * 0.2);
            }
        }

        // 6 points if the day in the purchase date is odd.
        int day = Integer.parseInt(receipt.getPurchaseDate().split("-")[2]);
        if (day % 2 == 1) {
            points += 6;
        }

        // 10 points if the time of purchase is after 2:00pm and before 4:00pm.
        String[] timeParts = receipt.getPurchaseTime().split(":");
        int hour = Integer.parseInt(timeParts[0]);
        int minute = Integer.parseInt(timeParts[1]);
        if (hour == 14 || (hour == 15 && minute < 60)) {
            points += 10;
        }

        return points;
    }
}
