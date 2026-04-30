import { useState } from "react";
import { pay } from "../api/payout";

type PayFormProps = {
    onSuccess: () => void;
};

export default function PayForm({ onSuccess }: PayFormProps) {
    const [amount, setAmount] = useState<string>("");
    const [loading, setLoading] = useState(false);

    const handleSubmit = async () => {
        if (!amount) return;

        setLoading(true);

        try {
            const res = await pay({
                amount: parseInt(amount),
                bank_ac_id: "bank1",
            });
            alert(`Payout created with ID: ${res.id}`);
            onSuccess();
            setAmount("");
        } catch (error) {
            alert(`Error: ${error}`);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ marginTop: 20 }}>
            <input
                type="number"
                placeholder="Amount"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                disabled={loading}
            />
            <button onClick={handleSubmit} disabled={loading}>
                {loading ? "Processing..." : "Pay"}
            </button>
        </div>
    );
}