package com.example.payment.api;

import com.example.payment.model.Payment;
import com.example.payment.service.PaymentService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.net.URI;
import java.util.List;
import java.util.UUID;

@RestController
@RequestMapping("/api/payments")
public class PaymentController {
    private final PaymentService svc;

    public PaymentController(PaymentService svc) {
        this.svc = svc;
    }

    @PostMapping
    public ResponseEntity<Payment> create(@RequestBody CreatePaymentRequest req) {
        Payment p = svc.create(req.getAmount(), req.getCurrency());
        return ResponseEntity.created(URI.create("/api/payments/" + p.getId())).body(p);
    }

    @GetMapping("/{id}")
    public ResponseEntity<Payment> get(@PathVariable UUID id) {
        return svc.get(id).map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.notFound().build());
    }

    @GetMapping
    public List<Payment> list() {
        return svc.list();
    }

    @PostMapping("/{id}/capture")
    public ResponseEntity<Payment> capture(@PathVariable UUID id) {
        return svc.markCaptured(id).map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.notFound().build());
    }
}