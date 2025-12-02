package com.example.payment.service;

import com.example.payment.model.Payment;
import org.springframework.stereotype.Service;

import java.math.BigDecimal;
import java.time.Instant;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

@Service
public class PaymentService {
    private final Map<UUID, Payment> store = new ConcurrentHashMap<>();

    public Payment create(BigDecimal amount, String currency) {
        UUID id = UUID.randomUUID();
        Payment p = new Payment(id, amount, currency, "PENDING", Instant.now());
        store.put(id, p);
        return p;
    }

    public Optional<Payment> get(UUID id) {
        return Optional.ofNullable(store.get(id));
    }

    public List<Payment> list() {
        return new ArrayList<>(store.values());
    }

    public Optional<Payment> markCaptured(UUID id) {
        Payment p = store.get(id);
        if (p == null) return Optional.empty();
        p.setStatus("CAPTURED");
        return Optional.of(p);
    }
}