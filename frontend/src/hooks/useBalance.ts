import { useState, useEffect } from "react";

export function useBalance() {
    const [balance, setBalance] = useState<number>(0);

    const fetchBalance = async () => {
        try {
            const res = await fetch("http://127.0.0.1:8000/api/v1/balance/");
            const data = await res.json();
            setBalance(data.balance);
        } catch (err) {
            console.error("Failed to fetch balance:", err);
        }
    };

    useEffect(() => {
        let mounted = true;

        (async () => {
            try {
                const res = await fetch("http://127.0.0.1:8000/api/v1/balance/");
                const data = await res.json();
                if (mounted) {
                    setBalance(data.balance);
                }
            } catch (err) {
                if (mounted) {
                    console.error("Failed to fetch balance:", err);
                }
            }
        })();

        return () => {
            mounted = false;
        };
    }, []);

    return { balance, fetchBalance };
}