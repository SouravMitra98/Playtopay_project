interface Payout {
    id: number;
    status: string;
    amount: number;
}

interface Props {
    payouts: Payout[];
}

export default function PayTable({ payouts }: Props) {
    return (
        <table border={1} cellPadding={10}>
            <thead>
                <tr>
                    <th>
                        ID
                    </th>
                    <th>
                        Amount
                    </th>
                    <th>
                        Status
                    </th>
                </tr>
            </thead>
            <tbody>
                {
                    payouts.map((pay) => (
                        <tr key={pay.id}>
                            <td>{pay.id}</td>
                            <td>{pay.amount}</td>
                            <td style={{
                                color:
                                    pay.status === "completed" ? "green" :
                                        pay.status === "failed" ? "red" :
                                            pay.status === "processing" ? "orange" :
                                                "gray"
                            }}>{pay.status}</td>
                        </tr>
                    ))
                }
            </tbody>
        </table>
    );
}