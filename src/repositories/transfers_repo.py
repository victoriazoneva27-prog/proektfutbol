from src.database.db import (
    execute,
    fetch_all
)


def add_transfer(
        player_id,
        from_club_id,
        to_club_id,
        transfer_date
):

    execute("""
        INSERT INTO transfers(
            player_id,
            from_club_id,
            to_club_id,
            transfer_date
        )
        VALUES (?, ?, ?, ?)
    """, (
        player_id,
        from_club_id,
        to_club_id,
        transfer_date
    ))


def get_transfers_by_player(
        player_id
):

    return fetch_all("""
        SELECT
            transfers.transfer_date,
            fc.name,
            tc.name
        FROM transfers
        JOIN clubs fc
        ON fc.id = transfers.from_club_id
        JOIN clubs tc
        ON tc.id = transfers.to_club_id
        WHERE transfers.player_id=?
        ORDER BY transfers.transfer_date DESC
    """, (player_id,))


def get_transfers_by_club(
        club_id
):

    return fetch_all("""
        SELECT
            transfers.transfer_date,
            players.full_name,
            fc.name,
            tc.name
        FROM transfers
        JOIN players
        ON players.id = transfers.player_id
        JOIN clubs fc
        ON fc.id = transfers.from_club_id
        JOIN clubs tc
        ON tc.id = transfers.to_club_id
        WHERE transfers.from_club_id=?
        OR transfers.to_club_id=?
        ORDER BY transfers.transfer_date DESC
    """, (
        club_id,
        club_id
    ))