<script>
	// Simuler l'appel API pour récupérer les notifications
	let notifications = [
		{ id: 1, message: 'Document ajouté au Dossier 001', lu: false },
		{ id: 2, message: 'Dossier 002 validé', lu: true }
	];

	function markAsRead(id) {
		notifications = notifications.map((notif) =>
			notif.id === id ? { ...notif, lu: true } : notif
		);
	}
</script>

<div class="fixed bottom-4 right-4 w-full max-w-xs">
	{#each notifications as notification}
		<div class="mb-2 bg-{notification.lu ? 'F1F1F1' : 'D9D9D9'} rounded-lg p-4 shadow-lg">
			<p>{notification.message}</p>
			<button
				on:click={() => markAsRead(notification.id)}
				class="text-001C98 hover:text-F02532 mt-2">Marquer comme lu</button
			>
		</div>
	{/each}
</div>
