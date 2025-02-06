package com.example.receipt_processor.controller;

import com.example.receipt_processor.model.PointsResponse;
import com.example.receipt_processor.model.ReceiptRequest;
import com.example.receipt_processor.model.ReceiptResponse;
import com.example.receipt_processor.service.ReceiptService;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.NoSuchElementException;
import java.util.Optional;

@RestController
@RequestMapping("/receipts")
//@RequiredArgsConstructor
public class ReceiptController {

    private final ReceiptService receiptService;

    @Autowired
    public ReceiptController(ReceiptService receiptService) {
        this.receiptService = receiptService;
    }

    @PostMapping("/process")
    public ResponseEntity<ReceiptResponse> processReceipts(@Valid @RequestBody ReceiptRequest receipt){

        String id = receiptService.processReceipt(receipt);
        return ResponseEntity.ok(new ReceiptResponse(id));

    }

    @GetMapping("/{id}/points")
    public ResponseEntity<PointsResponse> getPoints(@PathVariable String id) {
        Optional<Integer> points = receiptService.getPoints(id);

        if (points.isPresent()) {
            return ResponseEntity.ok(new PointsResponse(points.get()));
        } else {
            throw new NoSuchElementException("No receipt found for ID: " + id);
        }
    }
}
